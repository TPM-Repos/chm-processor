![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_T_
    The type of the condition to add.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateCondition<T>(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10873.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) > [CreateCondition Method](topic10872.md) : CreateCondition<T>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    

Glossary Item Box

Creates and adds a new condition to the condition sequence. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateCondition(Of T As [Condition](topic10804.md))( _
       ByVal _title_ As String _
    ) As T  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
    Dim title As String
    Dim value As T
     
    value = instance.CreateCondition(Of T)(title)  
  
C#|   
---|---  
      
    
    public T CreateCondition<T>( 
       string _title_
    )
    where T: [Condition](topic10804.md)  
  
#### Parameters

 _title_
    

#### Type Parameters

_T_
    The type of the condition to add.

#### Return Value

The newly created condition.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The type specified in for the type parameter T isn't defined in a extension library.  
[DriveWorks.ItemExistsException](topic3561.md)| Thrown when a condition with the provided title already exists.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)   
[Overload List](topic10872.md)

©2024 DriveWorks Ltd. All Rights Reserved.
