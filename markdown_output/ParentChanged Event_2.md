Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ParentChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategory Class](topic4219.md) : ParentChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the parent is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ParentChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategory](topic4219.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ParentChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ParentChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstantCategory Class](topic4219.md)   
[ProjectConstantCategory Members](topic4220.md)


