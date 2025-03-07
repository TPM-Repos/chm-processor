Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BufferedRuleWithVersionHistory Class   
[Members](topic6036.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) : BufferedRuleWithVersionHistory Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides an implementation of the [IHasRule](topic5947.md) implementation which acts as a buffer between a rule, and a rule consumer. 

# Object Model

![](dotnetdiagramimages/image311.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Class BufferedRuleWithVersionHistory 
       Inherits [BufferedRule](topic6017.md)
       Implements [IHasRule](topic5947.md), [IHasRuleId](topic5957.md), [IHasRuleType](topic5969.md), [IHasRuleVersionHistory](topic5975.md), [DriveWorks.IHasRuleContext](topic2237.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [BufferedRuleWithVersionHistory](topic6035.md)  
  
C#|   
---|---  
      
    
    public class BufferedRuleWithVersionHistory : [BufferedRule](topic6017.md), [IHasRule](topic5947.md), [IHasRuleId](topic5957.md), [IHasRuleType](topic5969.md), [IHasRuleVersionHistory](topic5975.md), [DriveWorks.IHasRuleContext](topic2237.md)    
  
# Inheritance Hierarchy

System.Object  
[DriveWorks.Abstractions.BufferedRule](topic6017.md)  
**DriveWorks.Abstractions.BufferedRuleWithVersionHistory**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[BufferedRuleWithVersionHistory Members](topic6036.md)   
[DriveWorks.Abstractions Namespace](topic5939.md)


