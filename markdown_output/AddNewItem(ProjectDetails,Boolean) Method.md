Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddNewItem(ProjectDetails,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ChildSpecificationList Class](topic7547.md) : AddNewItem(ProjectDetails,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectDetail_
    The project to base the child specification context on.

_showUI_
    Whether or not the child specification's UI should be shown to the user.

Glossary Item Box

Creates a new child specification context. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function AddNewItem( _
       ByVal _projectDetail_ As [ProjectDetails](topic4330.md), _
       Optional ByVal _showUI_ As Boolean _
    ) As [SpecificationContext](topic11149.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ChildSpecificationList](topic7547.md)
    Dim projectDetail As [ProjectDetails](topic4330.md)
    Dim showUI As Boolean
    Dim value As [SpecificationContext](topic11149.md)
     
    value = instance.AddNewItem(projectDetail, showUI)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public [SpecificationContext](topic11149.md) AddNewItem( 
       [ProjectDetails](topic4330.md) _projectDetail_ ,
       bool _showUI_
    )  
  
#### Parameters

 _projectDetail_
    The project to base the child specification context on.
_showUI_
    Whether or not the child specification's UI should be shown to the user.

#### Return Value

The specification context that was created.

# Remarks

The specification context might have changed as there is a OnOpenChildSpecificationRequest event raised from the parent context. That will allow changes to be made to the context before this method is complete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ChildSpecificationList Class](topic7547.md)   
[ChildSpecificationList Members](topic7548.md)


