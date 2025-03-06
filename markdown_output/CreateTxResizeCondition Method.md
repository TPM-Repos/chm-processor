![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxResizeCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxResizeCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionRef_
    The reference to the condition to modify.

_newWidth_
    The new width of the condition, or null (Nothing in Visual Basic) to enable auto sizing.

Glossary Item Box

Creates a transaction which, when committed, will change the width of the specified condition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxResizeCondition( _
       ByVal _conditionRef_ As [ConditionRef](topic12843.md), _
       ByVal _newWidth_ As Nullable(Of Double) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionRef As [ConditionRef](topic12843.md)
    Dim newWidth As Nullable(Of Double)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxResizeCondition(conditionRef, newWidth)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxResizeCondition( 
       [ConditionRef](topic12843.md) _conditionRef_ ,
       Nullable<double> _newWidth_
    )  
  
#### Parameters

 _conditionRef_
    The reference to the condition to modify.
_newWidth_
    The new width of the condition, or null (Nothing in Visual Basic) to enable auto sizing.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


