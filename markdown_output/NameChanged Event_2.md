Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NameChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacro Class](topic11429.md) : NameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [Name](topic11446.md) property is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NameChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacro](topic11429.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.NameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> NameChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacro Class](topic11429.md)   
[SpecificationMacro Members](topic11430.md)


