Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAllControls Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ContainerControlBase Class](topic7684.md) : GetAllControls Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets collection of all child controls contained by the control. Including the control children's children. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAllControls() As IEnumerable(Of ControlBase)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ContainerControlBase](topic7684.md)
    Dim value As IEnumerable(Of ControlBase)
     
    value = instance.GetAllControls()  
  
C#|   
---|---  
      
    
    public IEnumerable<ControlBase> GetAllControls()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ContainerControlBase Class](topic7684.md)   
[ContainerControlBase Members](topic7685.md)


