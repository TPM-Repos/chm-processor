Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BatchActionInstancesAndComponents Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationSettings Class](topic15238.md) : BatchActionInstancesAndComponents Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether instances and components are deleted, suppressed, unsuppressed, hidden, or shown in batches. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property BatchActionInstancesAndComponents As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationSettings](topic15238.md)
    Dim value As Boolean
     
    instance.BatchActionInstancesAndComponents = value
     
    value = instance.BatchActionInstancesAndComponents  
  
C#|   
---|---  
      
    
    public bool BatchActionInstancesAndComponents {get; set;}  
  
# Remarks

Setting this to False will cause all instances and components to be deleted one-by-one which might slow down generation but provides a much more granular Model Insight exprience.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[GenerationSettings Members](topic15239.md)


