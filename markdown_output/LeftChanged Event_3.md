Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LeftChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [StartNode Class](topic7120.md) : LeftChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs whenever the [Left](topic7129.md) property's value has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event LeftChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StartNode](topic7120.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.LeftChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> LeftChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StartNode Class](topic7120.md)   
[StartNode Members](topic7121.md)


