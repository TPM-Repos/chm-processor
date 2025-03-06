![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxUpdateFormControlRectangles(String[],Rect[],Rect[]) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxUpdateFormControlRectangles Method](topic13138.md) : CreateTxUpdateFormControlRectangles(String[],Rect[],Rect[]) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlNames_
    The names of the form controls to modify.

_oldRectangles_
    The rectangles of the form controls before the change.

_newRectangles_
    The desired rectangles of the form controls after the change.

Glossary Item Box

Creates a transaction which, when committed, will update the rectangles of the specified controls. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxUpdateFormControlRectangles( _
       ByVal _controlNames_() As String, _
       ByVal _oldRectangles_() As Rect, _
       ByVal _newRectangles_() As Rect _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim controlNames() As String
    Dim oldRectangles() As Rect
    Dim newRectangles() As Rect
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxUpdateFormControlRectangles(controlNames, oldRectangles, newRectangles)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxUpdateFormControlRectangles( 
       string[] _controlNames_ ,
       Rect[] _oldRectangles_ ,
       Rect[] _newRectangles_
    )  
  
#### Parameters

 _controlNames_
    The names of the form controls to modify.
_oldRectangles_
    The rectangles of the form controls before the change.
_newRectangles_
    The desired rectangles of the form controls after the change.

#### Return Value

A transaction.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13138.md)


