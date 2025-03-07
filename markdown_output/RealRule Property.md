Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RealRule Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchResult Class](topic13227.md) : RealRule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the underlying [DriveWorks.Abstractions.IHasRule](topic5947.md) or a generic wrapper. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable ReadOnly Property RealRule As [IHasRule](topic5947.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchResult](topic13227.md)
    Dim value As [IHasRule](topic5947.md)
     
    value = instance.RealRule  
  
C#|   
---|---  
      
    
    public virtual [IHasRule](topic5947.md) RealRule {get;}  
  
#### Property Value

The [DriveWorks.Abstractions.IHasRule](topic5947.md) for this item.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleSearchResult Class](topic13227.md)   
[RuleSearchResult Members](topic13228.md)


