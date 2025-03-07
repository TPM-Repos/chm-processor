Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NodeCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowNodeCollection Class](topic7011.md) : NodeCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event raised when a node has been added to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NodeCreated As EventHandler(Of ExecutableNodeEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowNodeCollection](topic7011.md)
    Dim handler As EventHandler(Of ExecutableNodeEventArgs)
     
    AddHandler instance.NodeCreated, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ExecutableNodeEventArgs> NodeCreated  
  
# Event Data

The event handler receives an argument of type [ExecutableNodeEventArgs](topic6983.md) containing data related to this event. The following **ExecutableNodeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Node](topic6989.md)| The node that participated in the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowNodeCollection Class](topic7011.md)   
[FlowNodeCollection Members](topic7012.md)


