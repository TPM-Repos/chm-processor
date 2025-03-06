![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14368.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedViewCollection Class](topic14362.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sheetName_
    

_name_
    

Glossary Item Box

Adds a new view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _sheetName_ As String, _
       ByVal _name_ As String _
    ) As [CapturedView](topic14351.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CapturedViewCollection](topic14362.md)
    Dim sheetName As String
    Dim name As String
    Dim value As [CapturedView](topic14351.md)
     
    value = instance.Add(sheetName, name)  
  
C#|   
---|---  
      
    
    public [CapturedView](topic14351.md) Add( 
       string _sheetName_ ,
       string _name_
    )  
  
#### Parameters

 _sheetName_
    
_name_
    

#### Return Value

The newly created view.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedViewCollection Class](topic14362.md)   
[CapturedViewCollection Members](topic14363.md)

©2024 DriveWorks Ltd. All Rights Reserved.
