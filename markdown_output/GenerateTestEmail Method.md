![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerateTestEmail Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Email Class](topic2768.md) : GenerateTestEmail Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_details_
    

_ignoreRelativeAttachments_
    

Glossary Item Box

Generates and sends a test email. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub GenerateTestEmail( _
       ByVal _details_ As [EmailDocumentDetails](topic2793.md), _
       ByVal _ignoreRelativeAttachments_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Email](topic2768.md)
    Dim details As [EmailDocumentDetails](topic2793.md)
    Dim ignoreRelativeAttachments As Boolean
     
    instance.GenerateTestEmail(details, ignoreRelativeAttachments)  
  
C#|   
---|---  
      
    
    public void GenerateTestEmail( 
       [EmailDocumentDetails](topic2793.md) _details_ ,
       bool _ignoreRelativeAttachments_
    )  
  
#### Parameters

 _details_
    
_ignoreRelativeAttachments_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Email Class](topic2768.md)   
[Email Members](topic2769.md)


