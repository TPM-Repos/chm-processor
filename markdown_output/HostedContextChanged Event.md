Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HostedContextChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SpecificationHostControl Class](topic8979.md) : HostedContextChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [HostedContext](topic8990.md) value changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event HostedContextChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationHostControl](topic8979.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.HostedContextChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> HostedContextChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationHostControl Class](topic8979.md)   
[SpecificationHostControl Members](topic8980.md)


