from two_factor.admin import AdminSiteOTPRequired


class StaffAdminSite(AdminSiteOTPRequired):
    site_header = "RC Property · Staff workspace"
    site_title = "RC Property staff"
    index_title = "Manage projects and content"
    enable_nav_sidebar = True
