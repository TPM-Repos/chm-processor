![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviousCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : PreviousCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_previousStep_
    

_isNextEnabled_
    

_isPreviousEnabled_
    

_isFinishEnabled_
    

_isCancelEnabled_
    

Glossary Item Box

Attempts navigation to the previous wizard step. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function PreviousCore( _
       ByVal _previousStep_ As Control, _
       ByVal _isNextEnabled_ As Boolean, _
       ByVal _isPreviousEnabled_ As Boolean, _
       ByVal _isFinishEnabled_ As Boolean, _
       ByVal _isCancelEnabled_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim previousStep As Control
    Dim isNextEnabled As Boolean
    Dim isPreviousEnabled As Boolean
    Dim isFinishEnabled As Boolean
    Dim isCancelEnabled As Boolean
    Dim value As Boolean
     
    value = instance.PreviousCore(previousStep, isNextEnabled, isPreviousEnabled, isFinishEnabled, isCancelEnabled)  
  
C#|   
---|---  
      
    
    protected virtual bool PreviousCore( 
       Control _previousStep_ ,
       bool _isNextEnabled_ ,
       bool _isPreviousEnabled_ ,
       bool _isFinishEnabled_ ,
       bool _isCancelEnabled_
    )  
  
#### Parameters

 _previousStep_
    
_isNextEnabled_
    
_isPreviousEnabled_
    
_isFinishEnabled_
    
_isCancelEnabled_
    

#### Return Value

**true** if navigation succeeds.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


