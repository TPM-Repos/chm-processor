Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyRequirementsChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [IFlowNode Interface](topic6873.md) : NotifyRequirementsChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Called whenever the value of any mapped inputs or connections have changed And this node should reevaluate whether it can execute or not. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyRequirementsChanged()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IFlowNode](topic6873.md)
     
    instance.NotifyRequirementsChanged()  
  
C#|   
---|---  
      
    
    void NotifyRequirementsChanged()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IFlowNode Interface](topic6873.md)   
[IFlowNode Members](topic6874.md)


