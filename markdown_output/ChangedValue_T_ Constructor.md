![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangedValue<T> Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2493.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ChangedValue<T> Class](topic2487.md) : ChangedValue<T> Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldValue_
    The old value.

_newValue_
    the new value.

Glossary Item Box

Creates a new instance of the [ChangedValue<T>](topic2487.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _oldValue_ As T, _
       ByVal _newValue_ As T _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim oldValue As T
    Dim newValue As T
     
    Dim instance As New [ChangedValue(Of T)](topic2487.md)(oldValue, newValue)  
  
C#|   
---|---  
      
    
    public ChangedValue<T>( 
       T _oldValue_ ,
       T _newValue_
    )  
  
#### Parameters

 _oldValue_
    The old value.
_newValue_
    the new value.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ChangedValue<T> Class](topic2487.md)   
[ChangedValue<T> Members](topic2488.md)

©2024 DriveWorks Ltd. All Rights Reserved.
