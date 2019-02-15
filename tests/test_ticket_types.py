from core.controllers.ticket_types.ticket_types_controller import TicketTypesController

tt_control = TicketTypesController()
print(tt_control.read())
tt_control.create('super-good')
tt_control.update('mega',1)
tt_control.delete(1)