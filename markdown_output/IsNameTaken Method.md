Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsNameTaken Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) : IsNameTaken Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to check.

Glossary Item Box

Checks if the given name is occupied by a task in any of the collections managed by this accessor. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsNameTaken( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim name As String
    Dim value As Boolean
     
    value = instance.IsNameTaken(name)  
  
C#|   
---|---  
      
    
    public bool IsNameTaken( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name to check.

#### Return Value

True if a task exists in the accessor with the given name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)


