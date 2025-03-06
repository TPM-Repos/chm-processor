       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetGroupSetting(String,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2982.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) > [SetGroupSetting Method](topic2980.md) : SetGroupSetting(String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the setting.

_value_
    The value of the setting.

Glossary Item Box

Saves the named setting to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetGroupSetting( _
       ByVal _name_ As String, _
       ByVal _value_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim name As String
    Dim value As Boolean
     
    instance.SetGroupSetting(name, value)  
  
C#|   
---|---  
      
    
    public void SetGroupSetting( 
       string _name_ ,
       bool _value_
    )  
  
#### Parameters

 _name_
    The name of the setting.
_value_
    The value of the setting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)   
[Overload List](topic2980.md)

©2024 DriveWorks Ltd. All Rights Reserved.
