![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRange(String,String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5928.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [XmlTemplateDocument Class](topic5909.md) > [SetRange Method](topic5926.md) : SetRange(String,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be driven.

_formula_
    Formula of the range.

_comment_
    

Glossary Item Box

Sets/adds ranges to be driven. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetRange( _
       ByVal _name_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [XmlTemplateDocument](topic5909.md)
    Dim name As String
    Dim formula As String
    Dim comment As String
     
    instance.SetRange(name, formula, comment)  
  
C#|   
---|---  
      
    
    public void SetRange( 
       string _name_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _name_
    Name of the range to be driven.
_formula_
    Formula of the range.
_comment_
    

# ![](dotnetimages/collapse.gif)Remarks

A name must exactly equal XML file's range name.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[XmlTemplateDocument Class](topic5909.md)   
[XmlTemplateDocument Members](topic5910.md)   
[Overload List](topic5926.md)

©2024 DriveWorks Ltd. All Rights Reserved.
