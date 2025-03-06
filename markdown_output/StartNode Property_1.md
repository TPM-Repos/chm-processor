       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StartNode Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowBase Class](topic6999.md) : StartNode Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the first node in this flow that serves as the start point to which all other [IFlowNode](topic6873.md)s should be connected. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Property StartNode As [StartNode](topic7120.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowBase](topic6999.md)
    Dim value As [StartNode](topic7120.md)
     
    value = instance.StartNode  
  
C#|   
---|---  
      
    
    public abstract [StartNode](topic7120.md) StartNode {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowBase Class](topic6999.md)   
[FlowBase Members](topic7000.md)


