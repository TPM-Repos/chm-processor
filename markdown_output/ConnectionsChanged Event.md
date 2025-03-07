Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConnectionsChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacro Class](topic11429.md) : ConnectionsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever a connection between a property and an output in this macro has been created or removed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConnectionsChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacro](topic11429.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ConnectionsChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ConnectionsChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacro Class](topic11429.md)   
[SpecificationMacro Members](topic11430.md)


