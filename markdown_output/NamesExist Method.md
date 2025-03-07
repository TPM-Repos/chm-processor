Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NamesExist Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : NamesExist Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_names_
    The names to check.

Glossary Item Box

Checks the names to ensure they don't already exist in the design master. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function NamesExist( _
       ByVal _names_() As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim names() As String
    Dim value As Boolean
     
    value = instance.NamesExist(names)  
  
C#|   
---|---  
      
    
    public bool NamesExist( 
       string[] _names_
    )  
  
#### Parameters

 _names_
    The names to check.

#### Return Value

True if one or more of the names exist in the design master, false if names do not exist in the design master.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


