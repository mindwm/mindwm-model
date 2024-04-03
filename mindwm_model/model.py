from neomodel import (
        config, StructuredNode, StringProperty, IntegerProperty,
        UniqueIdProperty, RelationshipTo, RelationshipFrom, Relationship, One, OneOrMore,
        DateTimeProperty
        )

class MindwmUser(StructuredNode):
    username = StringProperty(required = True)
    host = RelationshipTo('MindwmHost', 'HAS_MINDWM_HOST')

class MindwmHost(StructuredNode):
    hostname = StringProperty(required = True)
    tmux = RelationshipTo('Tmux', 'HAS_TMUX')

class Tmux(StructuredNode):
    socket_path = StringProperty(required = True)
    session = RelationshipTo('TmuxSession', 'HAS_TMUX_SESSION')

class TmuxSession(StructuredNode):
    name = StringProperty(required = True)
    pane = RelationshipTo('TmuxPane', 'HAS_TMUX_PANE')

class TmuxPane(StructuredNode):
    pane_id = IntegerProperty(required = True)
    title = StringProperty()
    io_document = Relationship('IoDocument', 'HAS_IO_DOCUMENT')

class IoDocument(StructuredNode):
    uuid = StringProperty(unique_index=True, required = True)
    user_input = StringProperty(required = True)
    output = StringProperty(required = True)
    ps1 = StringProperty(required = True)
    time = DateTimeProperty(default_now = True)
    tmux_pane = Relationship('TmuxPane', 'HAS_IO_DOCUMENT')
