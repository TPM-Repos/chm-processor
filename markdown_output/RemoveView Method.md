       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveView Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewRegistrationService Interface](topic578.md) : RemoveView Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The culture-invariant name of the view to remove.

Glossary Item Box

Removes a view with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RemoveView( _
       ByVal _name_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IViewRegistrationService](topic578.md)
    Dim name As String
     
    instance.RemoveView(name)  
  
C#|   
---|---  
      
    
    void RemoveView( 
       string _name_
    )  
  
#### Parameters

 _name_
    The culture-invariant name of the view to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IViewRegistrationService Interface](topic578.md)   
[IViewRegistrationService Members](topic579.md)


