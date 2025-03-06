![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteCondition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13085.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionRef_
    The reference to the condition to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete the specified condition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteCondition( _
       ByVal _conditionRef_ As [ConditionRef](topic12843.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionRef As [ConditionRef](topic12843.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteCondition(conditionRef)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteCondition( 
       [ConditionRef](topic12843.md) _conditionRef_
    )  
  
#### Parameters

 _conditionRef_
    The reference to the condition to delete.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
