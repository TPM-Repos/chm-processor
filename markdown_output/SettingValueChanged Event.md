       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingValueChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic470.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : SettingValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the value of a setting changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event SettingValueChanged As EventHandler(Of SettingValueChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim handler As EventHandler(Of SettingValueChangedEventArgs)
     
    AddHandler instance.SettingValueChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler<SettingValueChangedEventArgs> SettingValueChanged  
  
# Event Data

The event handler receives an argument of type [SettingValueChangedEventArgs](topic975.md) containing data related to this event. The following **SettingValueChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SettingName](topic983.md)| Gets the name of the setting whose value changed.   
[SettingValue](topic984.md)| Gets the new value of the setting.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)

©2024 DriveWorks Ltd. All Rights Reserved.
