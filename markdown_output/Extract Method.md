![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Extract Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ProjectComponents Class](topic6229.md) : Extract Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentType_
    The type of component to remove.

Glossary Item Box

Removes components of the specified type from the collection and returns them in a new collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Extract( _
       ByVal _componentType_ As String _
    ) As [ProjectComponents](topic6229.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponents](topic6229.md)
    Dim componentType As String
    Dim value As [ProjectComponents](topic6229.md)
     
    value = instance.Extract(componentType)  
  
C#|   
---|---  
      
    
    public [ProjectComponents](topic6229.md) Extract( 
       string _componentType_
    )  
  
#### Parameters

 _componentType_
    The type of component to remove.

#### Return Value

A collection containing the extracted components.

# ![](dotnetimages/collapse.gif)Remarks

This method will cause all immediate children's capture data to be resolved.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectComponents Class](topic6229.md)   
[ProjectComponents Members](topic6230.md)


