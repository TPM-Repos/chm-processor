![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReplaceNamespaceDeclaration Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2380.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AdvancedXmlDocument Class](topic2364.md) : ReplaceNamespaceDeclaration Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_element_
    

_nsPrefix_
    

_nsUri_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub ReplaceNamespaceDeclaration( _
       ByRef _element_ As XElement, _
       ByVal _nsPrefix_ As String, _
       ByVal _nsUri_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [AdvancedXmlDocument](topic2364.md)
    Dim element As XElement
    Dim nsPrefix As String
    Dim nsUri As String
     
    instance.ReplaceNamespaceDeclaration(element, nsPrefix, nsUri)  
  
C#|   
---|---  
      
    
    protected void ReplaceNamespaceDeclaration( 
       ref XElement _element_ ,
       string _nsPrefix_ ,
       string _nsUri_
    )  
  
#### Parameters

 _element_
    
_nsPrefix_
    
_nsUri_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AdvancedXmlDocument Class](topic2364.md)   
[AdvancedXmlDocument Members](topic2365.md)

©2024 DriveWorks Ltd. All Rights Reserved.
