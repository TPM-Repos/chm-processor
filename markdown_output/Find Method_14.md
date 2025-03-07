Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Find Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) : Find Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the control to find.

_recursive_
    True to recurse, or false just to search immediate children.

Glossary Item Box

Finds a control with the specified name by performing a linear search. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Find( _
       ByVal _name_ As String, _
       ByVal _recursive_ As Boolean _
    ) As [ControlBase](topic7698.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim name As String
    Dim recursive As Boolean
    Dim value As [ControlBase](topic7698.md)
     
    value = instance.Find(name, recursive)  
  
C#|   
---|---  
      
    
    public [ControlBase](topic7698.md) Find( 
       string _name_ ,
       bool _recursive_
    )  
  
#### Parameters

 _name_
    The name of the control to find.
_recursive_
    True to recurse, or false just to search immediate children.

#### Return Value

The control that matches the given name, or a null reference (Nothing in Visual Basic) if nothing was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)


