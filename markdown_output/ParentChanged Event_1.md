Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ParentChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstant Class](topic4171.md) : ParentChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the constant's category is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ParentChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstant](topic4171.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ParentChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ParentChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstant Class](topic4171.md)   
[ProjectConstant Members](topic4172.md)


