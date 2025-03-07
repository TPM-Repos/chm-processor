Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenericRuleWithCustomName Class   
[Members](topic6064.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) : GenericRuleWithCustomName Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a simple implementation of the [IHasRule](topic5947.md) implementation with customized support for the MyName function. 

# Object Model

![](dotnetdiagramimages/image313.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public NotInheritable Class GenericRuleWithCustomName 
       Implements [IHasRule](topic5947.md), [IHasRuleType](topic5969.md), [DriveWorks.IHasRuleContext](topic2237.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenericRuleWithCustomName](topic6063.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public sealed class GenericRuleWithCustomName : [IHasRule](topic5947.md), [IHasRuleType](topic5969.md), [DriveWorks.IHasRuleContext](topic2237.md)    
  
# Inheritance Hierarchy

System.Object  
**DriveWorks.Abstractions.GenericRuleWithCustomName**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenericRuleWithCustomName Members](topic6064.md)   
[DriveWorks.Abstractions Namespace](topic5939.md)


