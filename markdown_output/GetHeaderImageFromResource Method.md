![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetHeaderImageFromResource Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : GetHeaderImageFromResource Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_resourceName_
    The name of the image resource.

Glossary Item Box

A helper function which gets an image which has been embedded as a resource in the implementing type's assembly. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function GetHeaderImageFromResource( _
       ByVal _resourceName_ As String _
    ) As Image  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim resourceName As String
    Dim value As Image
     
    value = instance.GetHeaderImageFromResource(resourceName)  
  
C#|   
---|---  
      
    
    protected Image GetHeaderImageFromResource( 
       string _resourceName_
    )  
  
#### Parameters

 _resourceName_
    The name of the image resource.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


