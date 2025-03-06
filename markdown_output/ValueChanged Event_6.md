ValueChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutput Class](topic7074.md) : ValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever the value of this output has been set. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ValueChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeOutput](topic7074.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ValueChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeOutput Class](topic7074.md)   
[NodeOutput Members](topic7075.md)


