Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AgentNotificationReceived Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : AgentNotificationReceived Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a notification is received from another session. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event AgentNotificationReceived As EventHandler(Of NotificationEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim handler As EventHandler(Of NotificationEventArgs)
     
    AddHandler instance.AgentNotificationReceived, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<NotificationEventArgs> AgentNotificationReceived  
  
# Event Data

The event handler receives an argument of type [NotificationEventArgs](topic10064.md) containing data related to this event. The following **NotificationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Message](topic10070.md)| Gets the notification message.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


