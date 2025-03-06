![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2371.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AdvancedXmlDocument Class](topic2364.md) : AddRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    A unique Id for the new rule.

_xpath_
    The XPath of the element being added.

_formula_
    The formula for the rule.

_comment_
    The rules comment.

Glossary Item Box

Creates and Adds a new [ProjectDocumentRule](topic4399.md) to the document. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddRule( _
       ByVal _ruleId_ As Guid, _
       ByVal _xpath_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [AdvancedXmlDocument](topic2364.md)
    Dim ruleId As Guid
    Dim xpath As String
    Dim formula As String
    Dim comment As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.AddRule(ruleId, xpath, formula, comment)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) AddRule( 
       Guid _ruleId_ ,
       string _xpath_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _ruleId_
    A unique Id for the new rule.
_xpath_
    The XPath of the element being added.
_formula_
    The formula for the rule.
_comment_
    The rules comment.

#### Return Value

The created [DriveWorks.Abstractions.IHasRule](topic5947.md) object.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AdvancedXmlDocument Class](topic2364.md)   
[AdvancedXmlDocument Members](topic2365.md)

©2024 DriveWorks Ltd. All Rights Reserved.
