Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGroupSettingAsBoolean(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) > [GetGroupSettingAsBoolean Method](topic2972.md) : GetGroupSettingAsBoolean(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the setting to retrieve.

Glossary Item Box

Gets the named setting from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetGroupSettingAsBoolean( _
       ByVal _name_ As String _
    ) As Nullable(Of Boolean)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim name As String
    Dim value As Nullable(Of Boolean)
     
    value = instance.GetGroupSettingAsBoolean(name)  
  
C#|   
---|---  
      
    
    public Nullable<bool> GetGroupSettingAsBoolean( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the setting to retrieve.

#### Return Value

The boolean value of the setting that was retrieved, or a null reference (Nothing in Visual Basic) if the setting was not present.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)   
[Overload List](topic2972.md)


