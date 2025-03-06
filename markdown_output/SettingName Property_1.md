SettingName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Messaging Namespace](topic10038.md) > [SetAgentSettingMessage Class](topic10079.md) : SettingName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the name of the setting value to be changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property SettingName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SetAgentSettingMessage](topic10079.md)
    Dim value As String
     
    value = instance.SettingName  
  
C#|   
---|---  
      
    
    public string SettingName {get;}  
  
# Remarks

see [StandardAgentSettingNames](topic10088.md) for collection of standard setting names that can be used.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SetAgentSettingMessage Class](topic10079.md)   
[SetAgentSettingMessage Members](topic10080.md)


