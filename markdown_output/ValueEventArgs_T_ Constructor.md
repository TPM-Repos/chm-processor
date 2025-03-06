![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValueEventArgs<T> Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5849.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ValueEventArgs<T> Class](topic5843.md) : ValueEventArgs<T> Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The item that is specific to this event.

Glossary Item Box

Creates a new instance of the [ValueEventArgs<T>](topic5843.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _value_ As T _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim value As T
     
    Dim instance As New [ValueEventArgs(Of T)](topic5843.md)(value)  
  
C#|   
---|---  
      
    
    public ValueEventArgs<T>( 
       T _value_
    )  
  
#### Parameters

 _value_
    The item that is specific to this event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ValueEventArgs<T> Class](topic5843.md)   
[ValueEventArgs<T> Members](topic5844.md)

©2024 DriveWorks Ltd. All Rights Reserved.
