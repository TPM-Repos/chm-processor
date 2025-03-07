Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function GetHeaderImageFromResource( _
       ByVal _resourceName_ As String _
    ) As Image  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


