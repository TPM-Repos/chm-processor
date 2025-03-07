Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConnectionAdded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutput Class](topic7074.md) : ConnectionAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever a connection has been made to this output. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConnectionAdded As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeOutput](topic7074.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ConnectionAdded, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ConnectionAdded  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeOutput Class](topic7074.md)   
[NodeOutput Members](topic7075.md)


