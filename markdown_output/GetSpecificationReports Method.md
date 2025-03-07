Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationReports Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : GetSpecificationReports Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The numerical identifier of the specification for which to get reports.

Glossary Item Box

Gets a specification's reports. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSpecificationReports( _
       ByVal _specificationId_ As Integer _
    ) As IEnumerable(Of ReportDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim value As IEnumerable(Of ReportDetails)
     
    value = instance.GetSpecificationReports(specificationId)  
  
C#|   
---|---  
      
    
    public IEnumerable<ReportDetails> GetSpecificationReports( 
       int _specificationId_
    )  
  
#### Parameters

 _specificationId_
    The numerical identifier of the specification for which to get reports.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


