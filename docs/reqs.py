import docutils

from sphinx.util.compat import Directive, make_admonition

class req_node(docutils.nodes.Admonition, docutils.nodes.Element):
    pass

class req_list(docutils.nodes.General, docutils.nodes.Element):
    pass

def visit_req_node(self, node):
    self.visit_admonition(node)

def depart_req_node(self, node):
    self.depart_admonition(node)

class RequirementlistDirective(Directive):
    def run(self):
        return [req_list('')]

class RequirementDirective(Directive):
    # this enables content in the directive
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = "req-%03d" % env.new_serialno('req')
        targetnode = docutils.nodes.target('', '', ids=[targetid])
        
        admonition = make_admonition(
            req_node, self.name, ['Interoperability Test Requirement'],
            self.options, self.content, self.lineno, self.content_offset,
            self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'req_all_reqs'):
            env.req_all_reqs = []
        env.req_all_reqs.append({
            'content': ' '.join(self.content),
            'docname': env.docname,
            'lineno': self.lineno,
            'target': targetnode,
        })

        return [targetnode] + admonition

def purge_reqs(app, env, docname):
    if hasattr(env, 'req_all_reqs'):
        env.req_all_reqs = [req for req in env.req_all_reqs
                            if req['docname'] != docname]

def process_req_nodes(app, doctree, fromdocname):
    env = app.builder.env

    for node in doctree.traverse(req_list):
        ul = docutils.nodes.bullet_list('')

        for req in env.req_all_reqs:
            uri = app.builder.get_relative_uri(fromdocname, req['docname'])
            uri += '#' + req['target']['refid']
            ref = docutils.nodes.reference('', '(ref)', refuri=uri)
            rq = docutils.nodes.paragraph('', req['content'] + ' ', ref)
            ul.append(docutils.nodes.list_item('', rq))

        node.replace_self(ul)

def setup(app):
    app.add_node(req_list)
    app.add_node(req_node,
                 html=(visit_req_node, depart_req_node),
                 latex=(visit_req_node, depart_req_node),
                 text=(visit_req_node, depart_req_node))

    app.add_directive('requirement', RequirementDirective)
    app.add_directive('requirementlist', RequirementlistDirective)
    app.connect('doctree-resolved', process_req_nodes)
    app.connect('env-purge-doc', purge_reqs)
