       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetAgentSettingMessage Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10085.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Messaging Namespace](topic10038.md) > [SetAgentSettingMessage Class](topic10079.md) : SetAgentSettingMessage Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_settingName_
    The name of the setting to be changed.

_value_
    The new value to set on the setting. This value MUST be serializable.

Glossary Item Box

Creates a new instance of the [SetAgentSettingMessage](topic10079.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _settingName_ As String, _
       ByVal _value_ As Object _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim settingName As String
    Dim value As Object
     
    Dim instance As New [SetAgentSettingMessage](topic10079.md)(settingName, value)  
  
C#|   
---|---  
      
    
    public SetAgentSettingMessage( 
       string _settingName_ ,
       object _value_
    )  
  
#### Parameters

 _settingName_
    The name of the setting to be changed.
_value_
    The new value to set on the setting. This value MUST be serializable.

# Remarks

see [StandardAgentSettingNames](topic10088.md) for collection of standard setting names that can be used.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SetAgentSettingMessage Class](topic10079.md)   
[SetAgentSettingMessage Members](topic10080.md)

©2024 DriveWorks Ltd. All Rights Reserved.
