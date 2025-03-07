Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetReports Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetReports Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The identifier of the component for which to write the report.

Glossary Item Box

Gets a specification's reports. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetReports( _
       ByVal _componentId_ As Guid _
    ) As IEnumerable(Of ReportDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim value As IEnumerable(Of ReportDetails)
     
    value = instance.GetReports(componentId)  
  
C#|   
---|---  
      
    
    public IEnumerable<ReportDetails> GetReports( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The identifier of the component for which to write the report.

#### Return Value

An array of reports for the specified component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


