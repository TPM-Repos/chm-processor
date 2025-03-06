       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowDisplayFilesGroupSettingChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2957.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GeneralGroupSettings Class](topic2940.md) : ShowDisplayFilesGroupSettingChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [Group.SettingChanged](topic3021.md) event has been fired for the Show Display Files setting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ShowDisplayFilesGroupSettingChanged As EventHandler(Of SettingChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GeneralGroupSettings](topic2940.md)
    Dim handler As EventHandler(Of SettingChangedEventArgs)
     
    AddHandler instance.ShowDisplayFilesGroupSettingChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SettingChangedEventArgs> ShowDisplayFilesGroupSettingChanged  
  
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

©2024 DriveWorks Ltd. All Rights Reserved.
