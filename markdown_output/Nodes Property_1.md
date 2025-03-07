Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Nodes Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowBase Class](topic6999.md) : Nodes Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all nodes that have been added to this flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Property Nodes As [FlowNodeCollection](topic7011.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowBase](topic6999.md)
    Dim value As [FlowNodeCollection](topic7011.md)
     
    value = instance.Nodes  
  
C#|   
---|---  
      
    
    public abstract [FlowNodeCollection](topic7011.md) Nodes {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowBase Class](topic6999.md)   
[FlowBase Members](topic7000.md)


