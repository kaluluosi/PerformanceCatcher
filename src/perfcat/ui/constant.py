import enum

class ButtonStyle(enum.Enum):
    primary = "primary"
    success = "success"
    warning = "warning"
    danger = "danger"
    info = "info"

Color = {   
    'primary' : '#1b1e23',
    'success' : '#67c23a',
    'warning' : '#e6a23c',
    'danger'  : '#f56c6c',
    'info'    : '#909399'
}