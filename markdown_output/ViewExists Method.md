       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ViewExists Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewRegistrationService Interface](topic578.md) : ViewExists Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the view.

Glossary Item Box

Gets whether or not a view already exists with the provided name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ViewExists( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IViewRegistrationService](topic578.md)
    Dim name As String
    Dim value As Boolean
     
    value = instance.ViewExists(name)  
  
C#|   
---|---  
      
    
    bool ViewExists( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the view.

#### Return Value

True if a view exists with the provided name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IViewRegistrationService Interface](topic578.md)   
[IViewRegistrationService Members](topic579.md)


