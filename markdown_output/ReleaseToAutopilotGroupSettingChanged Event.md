ReleaseToAutopilotGroupSettingChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GeneralGroupSettings Class](topic2940.md) : ReleaseToAutopilotGroupSettingChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [Group.SettingChanged](topic3021.md) event has been fired for the Release To Autopilot setting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ReleaseToAutopilotGroupSettingChanged As EventHandler(Of SettingChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GeneralGroupSettings](topic2940.md)
    Dim handler As EventHandler(Of SettingChangedEventArgs)
     
    AddHandler instance.ReleaseToAutopilotGroupSettingChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SettingChangedEventArgs> ReleaseToAutopilotGroupSettingChanged  
  
# Event Data

The event handler receives an argument of type [SettingChangedEventArgs](topic5288.md) containing data related to this event. The following **SettingChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SettingName](topic5296.md)| Gets the name of the setting that was changed.   
[SettingValue](topic5297.md)| Gets the new value of the setting that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GeneralGroupSettings Class](topic2940.md)   
[GeneralGroupSettings Members](topic2941.md)


